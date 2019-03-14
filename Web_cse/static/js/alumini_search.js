
function displayOptions(valueOfOption){
  if (valueOfOption==='flname'){
    document.getElementById('nameId').style.display="block";
    document.getElementById('rollId').style.display="none";
  }

  else if (valueOfOption==='roll') {
    document.getElementById('rollId').style.display="block";
    document.getElementById('nameId').style.display="none";
  }
}


function invisibleOptions(){
  document.getElementById('nameId').style.display="none";
  document.getElementById('rollId').style.display="none";
  //document.getElementById('tabular_data').style.display="none";
}


