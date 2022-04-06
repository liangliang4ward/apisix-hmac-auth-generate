
var accessKey = "xxx";
var secret="xxx";

var path = pm.request.url.getPath();
var query=pm.request.url.query;
var queryArray=[];
for(index in query.members){
    var member= query.members[index];
    var value = member["value"];
    if(member["value"]==null){
        value = ""
    }
    var queryKeyValue = encodeURIComponent(member["key"])+"="+encodeURIComponent(value);
    queryArray.push(queryKeyValue);
}
queryArray.sort();
var queryString = queryArray.join("&");


var date = (new Date()).toGMTString();

var singString = pm.request.method+"\n"+path+"\n"+queryString+"\n"+accessKey+"\n"+date+"\n";
console.log(singString)
var hash = CryptoJS.HmacSHA256(singString, secret);
var hashInBase64 = CryptoJS.enc.Base64.stringify(hash);

pm.environment.set("X-HMAC-ACCESS-KEY",accessKey);
pm.environment.set("X-HMAC-SIGNATURE",hashInBase64);
pm.environment.set("X-HMAC-ALGORITHM","hmac-sha256");
pm.environment.set("Date",date);
