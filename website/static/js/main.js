// menu icon pop up
document.getElementById("bars").addEventListener("click", () => {
  //document.querySelector("#menu-items").style.display = "block";

  document.querySelector("#menu-items ul").style.display = "block";
  setTimeout(() => {
    document.getElementById("menu-items").style.height = "100vh"
    document.querySelector("#menu-items ul").style.opacity = "1"
    document.getElementById("close-icon").style.opacity = '1'
    document.getElementById("close-icon").style.display = "block"

  }, 1000)
})

// menu icon close
document.getElementById("close-icon").addEventListener("click", () => {
  document.querySelector("#menu-items ul").style.display = "none";
  document.getElementById("close-icon").style.display = "none"
  setTimeout(() => {
    document.getElementById("menu-items").style.height = '0vh'
    document.querySelector("#menu-items ul").style.opacity = "0"
    document.getElementById("close-icon").style.opacity = '0'
  }, 1000)
  // document.querySelector("#menu-items").style.display = "none";

})

document.getElementById("close-message").addEventListener("click", () => {
  document.getElementById("message-div").style.display= "none"
})
