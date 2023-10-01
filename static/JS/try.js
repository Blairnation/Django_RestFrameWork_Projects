// Modify your existing JavaScript to handle the image popup
var openImage = document.getElementById("openImage");
var imagePopup = document.getElementById("imagePopup");
var closeImage = document.getElementById("closeImage");

openImage.addEventListener("click", function() {
  imagePopup.classList.add("show");
});

closeImage.addEventListener("click", function() {
  imagePopup.classList.remove("show");
});


