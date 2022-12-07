//const s = document.querySelector('.sky')
//const p = document.querySelector('.plates');
//var root = document.querySelector(':root');
//var rootS = getComputedStyle(document.querySelector(':root'));

 //let lastKnownScrollPosition = 0;
 //let ticking = false;
// let LastScrollY = 0;
 
// function doSomething(scrollPos) {
 // if(scrollY >= 1100 && scrollY <= 2100){
 //   var transformY = rootS.getPropertyValue('--transformYSky');

 //     if(LastScrollY < scrollY){
 //       transformY = transformY - 1;
  //    }else{
  //      transformY = parseInt(transformY) + 1;
  //    }
  //    root.style.setProperty('--transformYSky', transformY);
 // }

 // LastScrollY = scrollY;
 //}

//function test(){

  //requestAnimationFrame(test);
//}

//requestAnimationFrame(test);
 //document.addEventListener('scroll', test, {passive: true});

var playerField = document.querySelector('.field-players');
var fieldFormations = document.querySelector('.field-formations');
var playerCarousel = document.querySelector('.player-carousel');
var playerSpots = document.querySelectorAll('.field-player');

 function showPlayerField(formation){
  playerField.classList.add('show');
  playerField.classList.add(formation);

  fieldFormations.classList.add('hide');
 }

 function addPlayer(playerCard){
  playerSpots.forEach(element => {
    if(element.classList.contains('red')){
      element.children[1].innerHTML = '<label>' + playerCard.id + '</label>';
    }   
  });
  playerCard.classList.add('hide');
 }

 function showCarousel(element){

  playerSpots.forEach(element => {
    element.classList.remove('red');
  });

  element.classList.add('red');
  playerCarousel.classList.add('showFlex');
 }

