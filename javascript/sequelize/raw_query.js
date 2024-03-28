// ################ Raw Queries   ###############

const { QueryTypes } = require("sequelize");
const users = await sequelize.query("SELECT * FROM `users`", { type: QueryTypes.SELECT });
// We didn't need to destructure the result here - the results were returned directly

// ################  Replacements  ###############

const { QueryTypes } = require("sequelize");

await sequelize.query("SELECT * FROM projects WHERE status = ?", {
  replacements: ["active"],
  type: QueryTypes.SELECT,
});

await sequelize.query("SELECT * FROM projects WHERE status = :status", {
  replacements: { status: "active" },
  type: QueryTypes.SELECT,
});

const totalAmount = await sequelize.query('SELECT SUM(price * quantity) AS totalSum FROM "Order_variants" WHERE id IN (:ordervariantIds)', {
  replacements: { ordervariantIds: orderVariantIds },
  type: sequelize.QueryTypes.SELECT,
});

// In the context of your SQL query, using backticks is beneficial because it allows you to write the query on multiple lines without explicitly concatenating strings. It also supports string interpolation, making it convenient to inject variables directly into the string.
const orderVariantIdsResult = await sequelize.query(
  `
      SELECT CAST("Ship_rocket_orderitems"."sku" AS INTEGER) as order_variant_id
      FROM "Ship_rocket_orders"
      JOIN "Ship_rocket_orderitems" ON "Ship_rocket_orders".id = "Ship_rocket_orderitems"."ShipRocketOrderId"
      WHERE "Ship_rocket_orders".shiprocket_order_id = :order_id
      `,
  {
    replacements: { order_id },
    type: sequelize.QueryTypes.SELECT,
  }
);
