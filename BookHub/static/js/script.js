$(document).ready(function(){
  $('.slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
  autoplaySpeed: 2000,
  });
});

document.addEventListener('DOMContentLoaded', () => {
   const burger = document.querySelector('.navbar-burger');
   const menu = document.querySelector('.navbar-menu');
   const con = document.querySelector('.navbar-content')
   burger.addEventListener('click', () => {
     menu.classList.toggle('hidden');
   });
   document.addEventListener('click', (event) => {
       if (!con.contains(event.target) && !burger.contains(event.target)) {
         menu.classList.add('hidden');
       }
     });
 });

document.addEventListener("DOMContentLoaded", function() {
  var searchInput = document.querySelector("#searchInput");

  searchInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
      event.preventDefault();
      var searchTerm = searchInput.value.trim(); 
      window.location.href = "/catalog?search=" + encodeURIComponent(searchTerm);
    }
  });
});

function resetFilters() {
   document.getElementById("author").value = ""; 
   document.getElementById("genre").selectedIndex = 0;
 }

 

  