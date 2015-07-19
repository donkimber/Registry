
WVR = {}

function report(str) {
   console.log(str);
}

function addRequest(req, doneFn)
{
      var url = "/reg_addrequest/";
      var qs = objToQueryStr(req);
      if (qs)
	  url += "?"+qs;
      //url += "?name="+req.name;
      //url += "&text="+req.text;
      report("url: "+url);
      $.getJSON(url, function(obj) {
          report("got back: "+JSON.stringify(obj));
          if (doneFn)
             doneFn(obj);
      });
}

objToQueryStr = function(obj) {
    report("objToQueryStr: "+JSON.stringify(obj));
    var str = [];
    for(var p in obj) {
	if (obj.hasOwnProperty(p)) {
	    str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
	}
    }
    return str.join("&");
}

//http://stackoverflow.com/questions/901115/how-can-i-get-query-string-values-in-javascript
function queryStrToObj(a) {
    if (a == "") return {};
    a = a.split("&");
    var b = {};
    for (var i = 0; i < a.length; ++i)
    {
        var p=a[i].split('=', 2);
        if (p.length == 1)
            b[p[0]] = "";
        else
            b[p[0]] = decodeURIComponent(p[1].replace(/\+/g, " "));
    }
    return b;
}

WVR.report = report
WVR.addRequest = addRequest;
WVR.queryStrToObj = queryStrToObj
WVR.objToQueryStr = objToQueryStr
