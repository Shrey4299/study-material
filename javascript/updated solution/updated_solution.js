class EventAggregator {
  constructor() {
    this.aggregations = {};
  }

  createMeta(aggregationMeta) {
    const { aggregationName, eventType, aggregationType, aggregationField, filterRules, timeInterval, slideInterval } = aggregationMeta;
    if (!this.aggregations[aggregationType]) {
      this.aggregations[aggregationType] = {};
    }
    this.aggregations[aggregationType][aggregationName] = {
      eventType,
      aggregationField,
      filterRules,
      timeInterval,
      slideInterval,
      result: {},
    };
  }

  computeAggregates(event) {
    for (const aggregationType in this.aggregations) {
      for (const aggregationName in this.aggregations[aggregationType]) {
        const aggregationMeta = this.aggregations[aggregationType][aggregationName];
        if (event.eventType === aggregationMeta.eventType) {
          if (aggregationType === "count") {
            this.countDistinctApps(aggregationMeta, event);
          } else if (aggregationType === "sum") {
            this.calculateTotalSum(aggregationMeta, event);
          }
        }
      }
    }
  }

  countDistinctApps(aggregationMeta, event) {
    const userId = this.getUserId(event);
    const appName = this.getAppName(event);

    if (!aggregationMeta.result[userId]) {
      aggregationMeta.result[userId] = [];
    }

    if (!aggregationMeta.result[userId].includes(appName)) {
      aggregationMeta.result[userId].push(appName);
    }
  }

  calculateTotalSum(aggregationMeta, event) {
    const userId = this.getUserId(event);
    const field = this.getAggregationFieldValue(aggregationMeta, event);

    if (!aggregationMeta.result[userId]) {
      aggregationMeta.result[userId] = 0;
    }

    aggregationMeta.result[userId] += field;
  }

  passesFilterRules(event, filterRules, timeInterval) {
    return (
      filterRules.every((rule) => {
        const { field, op, value } = rule;
        const fieldValue = this.getNestedValue(event, field);
        switch (op) {
          case "gt":
            return fieldValue > value;
          default:
            return true;
        }
      }) && this.isWithinTimeWindow(event, timeInterval)
    );
  }

  isWithinTimeWindow(event, timeInterval) {
    const currentTime = new Date().getTime();
    const eventTime = new Date(event.timestamp).getTime();
    return currentTime - eventTime <= timeInterval * 60 * 1000;
  }

  getNestedValue(object, path) {
    const keys = path.split(".");
    return keys.reduce((value, key) => (value ? value[key] : undefined), object);
  }

  getUserId(event) {
    return event.eventData.userId || "undefined";
  }

  getAppName(event) {
    return event.eventData.appName || "undefined";
  }

  getSpaceInMb(event) {
    return event.eventData.spaceInMb || 0;
  }

  getBattery(event) {
    return event.eventData.battery || 0;
  }

  getResult(aggregationType) {
    const result = {};
    for (const aggregationName in this.aggregations[aggregationType]) {
      result[aggregationName] = this.aggregations[aggregationType][aggregationName].result;
    }
    return result;
  }

  getAggregation(aggregationName, keyValue, aggregationType) {
    const aggregationMeta = this.aggregations[aggregationType][aggregationName];
    if (!aggregationMeta || !aggregationMeta.result[keyValue]) {
      return undefined;
    }

    return aggregationMeta.result[keyValue];
  }

  getAggregationFieldValue(aggregationMeta, event) {
    const { aggregationField } = aggregationMeta;
    return this.getNestedValue(event, aggregationField);
  }
}

const eventAggregator = new EventAggregator();

const installCountDistinctUserMeta = {
  aggregationName: "installCountDistinctUser",
  eventType: "APP_INSTALL_COMPLETED",
  aggregationType: "count",
  aggregationField: "eventData.userId",
  filterRules: [],
};

const totalSpaceUserMeta = {
  aggregationName: "totalSpaceUser",
  eventType: "APP_INSTALL_COMPLETED",
  aggregationType: "sum",
  aggregationField: "eventData.spaceInMb",
  filterRules: [],
};

const totalBatteryMeta = {
  aggregationName: "totalBattery",
  eventType: "APP_INSTALL_COMPLETED",
  aggregationType: "sum",
  aggregationField: "eventData.battery",
  filterRules: [],
};

const installCountUserMeta = {
  aggregationName: "installCountUser",
  eventType: "APP_INSTALL_COMPLETED",
  aggregationType: "count",
  aggregationField: "eventData.userId",
  timeInterval: 2,
  slideInterval: 1,
  filterRules: [
    {
      field: "eventData.spaceInMb",
      op: "gt",
      value: 2,
    },
  ],
};

// Create Aggregations
eventAggregator.createMeta(installCountDistinctUserMeta);
eventAggregator.createMeta(totalSpaceUserMeta);
eventAggregator.createMeta(totalBatteryMeta);
eventAggregator.createMeta(installCountUserMeta);

// Example events
const events = [
  { eventType: "APP_INSTALL_COMPLETED", eventData: { userId: "u001", appName: "app1", spaceInMb: 2, battery: 90 } },
  { eventType: "APP_INSTALL_COMPLETED", eventData: { userId: "u002", appName: "app2", spaceInMb: 3, battery: 90 } },
  { eventType: "APP_INSTALL_COMPLETED", eventData: { userId: "u001", appName: "app3", spaceInMb: 4, battery: 90 } },
  { eventType: "APP_INSTALL_COMPLETED", eventData: { userId: "u002", appName: "app4", spaceInMb: 1, battery: 90 } },
  { eventType: "APP_INSTALL_COMPLETED", eventData: { userId: "u003", appName: "app5", spaceInMb: 5, battery: 90 } },
  { eventType: "APP_INSTALL_COMPLETED", eventData: { userId: "u004", appName: "app3", spaceInMb: 4, battery: 90 } },
  { eventType: "APP_INSTALL_COMPLETED", eventData: { userId: "u004", appName: "app5", spaceInMb: 5, battery: 90 } },
];

// Consume events
events.forEach((event) => {
  eventAggregator.computeAggregates(event);
});

// Get Aggregations for distinct apps installed by each user
const installCountDistinctResult = eventAggregator.getResult("count");
console.log("Following are the aggregations created for distinct apps installed by each user:");
console.log('"installCountDistinctUser":', installCountDistinctResult["installCountDistinctUser"]);

// Get Aggregations for total space utilized by each user
const totalSpaceResult = eventAggregator.getResult("sum");
console.log("Following are the aggregations created for total space utilized by each user:");
console.log('"totalSpaceUser":', totalSpaceResult["totalSpaceUser"]);

// Get Aggregations for total battery utilized by each user
const totalBatteryResult = eventAggregator.getResult("sum");
console.log("Following are the aggregations created for total battery utilized by each user:");
console.log('"totalBattery":', totalBatteryResult["totalBattery"]);


