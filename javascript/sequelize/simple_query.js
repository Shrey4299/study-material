// ################ Simple INSERT queries  ###############

const user = await User.create(
  {
    username: "alice123",
    isAdmin: true,
  },
  { fields: ["username"] }
);
// let's assume the default of isAdmin is false
console.log(user.username); // 'alice123'
console.log(user.isAdmin); // false

// ################ Simple SELECT queries  ###############

const users = await User.findAll();

Model.findAll({
  attributes: ["foo", "bar"],
});
// SELECT foo, bar FROM ...

Model.findAll({
  attributes: ["foo", [sequelize.fn("COUNT", sequelize.col("hats")), "n_hats"], "bar"],
});
// SELECT foo, COUNT(hats) AS n_hats, bar FROM ...

// ################ Applying WHERE clauses  ###############

Post.findAll({
  where: {
    authorId: 2,
  },
});
// SELECT * FROM post WHERE authorId = 2;

const { Op } = require("sequelize");
Post.findAll({
  where: {
    [Op.and]: [{ authorId: 12 }, { status: "active" }],
  },
});
// SELECT * FROM post WHERE authorId = 12 AND status = 'active';

const { Op } = require("sequelize");
Post.findAll({
  where: {
    [Op.or]: [{ authorId: 12 }, { authorId: 13 }],
  },
});

Model.findAll({
  where: { a: { [Op.eq]: 2 } },
});
// SELECT * FROM post WHERE authorId = 12 OR authorId = 13;

// ################ Operators   ###############

const { Op } = require("sequelize");
Post.findAll({
  where: {
    [Op.and]: [{ a: 5 }, { b: 6 }], // (a = 5) AND (b = 6)
    [Op.or]: [{ a: 5 }, { b: 6 }], // (a = 5) OR (b = 6)
    someAttribute: {
      // Basics
      [Op.eq]: 3, // = 3
      [Op.ne]: 20, // != 20
      [Op.is]: null, // IS NULL
      [Op.not]: true, // IS NOT TRUE
      [Op.or]: [5, 6], // (someAttribute = 5) OR (someAttribute = 6)

      // Using dialect specific column identifiers (PG in the following example):
      [Op.col]: "user.organization_id", // = "user"."organization_id"

      // Number comparisons
      [Op.gt]: 6, // > 6
      [Op.gte]: 6, // >= 6
      [Op.lt]: 10, // < 10
      [Op.lte]: 10, // <= 10
      [Op.between]: [6, 10], // BETWEEN 6 AND 10
      [Op.notBetween]: [11, 15], // NOT BETWEEN 11 AND 15

      // Other operators

      [Op.all]: sequelize.literal("SELECT 1"), // > ALL (SELECT 1)

      [Op.in]: [1, 2], // IN [1, 2]
      [Op.notIn]: [1, 2], // NOT IN [1, 2]

      [Op.like]: "%hat", // LIKE '%hat'
      [Op.notLike]: "%hat", // NOT LIKE '%hat'
      [Op.startsWith]: "hat", // LIKE 'hat%'
      [Op.endsWith]: "hat", // LIKE '%hat'
      [Op.substring]: "hat", // LIKE '%hat%'
      [Op.iLike]: "%hat", // ILIKE '%hat' (case insensitive) (PG only)
      [Op.notILike]: "%hat", // NOT ILIKE '%hat'  (PG only)
      [Op.regexp]: "^[h|a|t]", // REGEXP/~ '^[h|a|t]' (MySQL/PG only)
      [Op.notRegexp]: "^[h|a|t]", // NOT REGEXP/!~ '^[h|a|t]' (MySQL/PG only)
      [Op.iRegexp]: "^[h|a|t]", // ~* '^[h|a|t]' (PG only)
      [Op.notIRegexp]: "^[h|a|t]", // !~* '^[h|a|t]' (PG only)

      [Op.any]: [2, 3], // ANY (ARRAY[2, 3]::INTEGER[]) (PG only)
      [Op.match]: Sequelize.fn("to_tsquery", "fat & rat"), // match text search for strings 'fat' and 'rat' (PG only)

      // In Postgres, Op.like/Op.iLike/Op.notLike can be combined to Op.any:
      [Op.like]: { [Op.any]: ["cat", "hat"] }, // LIKE ANY (ARRAY['cat', 'hat'])

      // There are more postgres-only range operators, see below
    },
  },
});

// ################ Operator Example ###############

Foo.findAll({
  where: {
    rank: {
      [Op.or]: {
        [Op.lt]: 1000,
        [Op.eq]: null,
      },
    },
    // rank < 1000 OR rank IS NULL

    title: {
      [Op.or]: [
        {
          title: {
            [Op.like]: "Boat%",
          },
        },
        {
          description: {
            [Op.like]: "%boat%",
          },
        },
      ],
    },
    // title LIKE 'Boat%' OR description LIKE '%boat%'
  },
});

// ################ Simple UPDATE queries   ###############

// Change everyone without a last name to "Doe"
await User.update(
  { lastName: "Doe" },
  {
    where: {
      lastName: null,
    },
  }
);

// ################ Simple DELETE queries   ###############
// Delete everyone named "Jane"
await User.destroy({
  where: {
    firstName: "Jane",
  },
});

// ################ Creating in bulk   ###############
const captains = await Captain.bulkCreate([{ name: "Jack Sparrow" }, { name: "Davy Jones" }]);

// ################ Grouping   ###############
Project.findAll({ group: "name" });
// yields 'GROUP BY name'

// ################ Limits and Pagination   ###############
// Skip 5 instances and fetch the 5 after that
Project.findAll({ offset: 5, limit: 5 });

// ################ max, min and sum   ###############
await User.max("age"); // 40
await User.max("age", { where: { age: { [Op.lt]: 20 } } }); // 10
await User.min("age"); // 5
await User.min("age", { where: { age: { [Op.gt]: 5 } } }); // 10
await User.sum("age"); // 55
await User.sum("age", { where: { age: { [Op.gt]: 5 } } }); // 50

// ################  increment, decrement  ###############

await User.increment({ age: 5 }, { where: { id: 1 } }); // Will increase age to 15
await User.increment({ age: -5 }, { where: { id: 1 } }); // Will decrease age to 5

// ################  count  ###############

const counts = await sequelize.models.Lead.findAll({
  attributes: [
    "status",
    [sequelize.fn("COUNT", sequelize.col("status")), "statusCount"],
    "source",
    [sequelize.fn("COUNT", sequelize.col("source")), "sourceCount"],
    "type",
    [sequelize.fn("COUNT", sequelize.col("type")), "typeCount"],
  ],
  group: ["status", "source", "type"],
});

// ################  includes  ###############

const products = await sequelize.models.Product.findAndCountAll({
  offset: pagination.offset,
  limit: pagination.limit,
  order: [["createdAt", "DESC"]],
  where: { ...(category_id ? { CategoryId: category_id } : {}) },
  distinct: true,
  include: [
    {
      model: sequelize.models.Variant,
      as: "variants",
      ...(query.price && {
        where: {
          price: {
            [Op.between]: [minPrice, maxPrice],
          },
        },
      }),
      include: ["gallery", "thumbnail"],
    },
    "tags",
    "gallery",
    "thumbnail",
  ],
});

const products2 = await sequelize.models.Product.findAndCountAll({
  include: [
    {
      model: sequelize.models.Collection,
      as: "collections",
      where: { id: id },
      include: ["category", "variants"],
    },
  ],
  limit: pagination.limit,
  offset: pagination.offset,
});

findAll({
  where: {
    age: {
      [Op.gt]: 13,
    },
  },
});
