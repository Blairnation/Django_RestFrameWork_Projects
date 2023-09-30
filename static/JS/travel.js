var pic = document.getElementById('pic-button')
pic.addEventListener('load',function(e){
  document.getElementById('gh1').classList.add("hidden")
})
pic.addEventListener('click',function(e){
  document.getElementById('gh1').classList.remove("hidden")
})
