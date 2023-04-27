async function getResult() {
    try {
      const response = await fetch("/get_result");
      const result = await response.text();
      document.getElementById("result").innerHTML = result;
    } catch (error) {
      console.error(error);
    }
  }
  
  getResult();
  