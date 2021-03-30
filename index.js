/*const fetch = require('node-fetch');
let url = "https://api.github.com/users/manishmshiva";

let settings = { method: "Post" };
fetch(url)
    .then(res => res.text())
    .then(text => console.log(text))*/
const fetch = require('node-fetch');
var mysql = require('mysql'); 
fetch('https://jsonplaceholder.typicode.com/users')
    .then(res => res.json())
    .then(json => {
        console.log("First user in the array:");
        console.log(json[0]);
        console.log("Name of the first user in the array:");
        console.log(json[0].name);
var con = mysql.createConnection({  
host: "localhost",  
user: "root",  
password: "",  
database: "sample"  
});  
con.connect(function(err) {  
if (err) throw err;  
console.log("Connected!");  
var sql = "INSERT INTO employee (id, name, email, website) VALUES ?";  
var values = [  
[json[0].id,json[0].name,json[0].email,json[0].website]
];  
con.query(sql, [values], function (err, result) {  
if (err) throw err;  
console.log("Number of records inserted: " + result.affectedRows);  
});  
});  
})
 
