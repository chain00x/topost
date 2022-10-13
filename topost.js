var formurlencoded = require('form-urlencoded');
var obj = {"a":1};

console.log(formurlencoded(obj, {
  ignorenull : true,
  sorted : true
}));
