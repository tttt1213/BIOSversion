function getResult() {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == 200) {
      var resultDiv = document.getElementById("result");
      resultDiv.innerHTML = xhr.responseText;
    }
  };
  xhr.open("GET", "app.py", true);
  xhr.send();
}

getResult();
