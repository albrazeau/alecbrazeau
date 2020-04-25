function titleLoad() {
    // Wrap every letter in a span
    var textWrapper = document.querySelector('.landing-title-text');
    textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

    anime.timeline()
    .add({
        targets: '.landing-title-text .letter',
        opacity: [0,1],
        easing: "easeInOutQuad",
        duration: 1500,
        delay: (el, i) => 150 * (i+1)
    });
}

function titleClick(){
    // Wrap every letter in a span
    var textWrapper = document.querySelector('.landing-title-text');
    textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");
    anime.timeline()
    .add({
        targets: '.landing-title-text .letter',
        opacity: [1,0],
        easing: "easeOutExpo",
        duration: 800,
        delay: (el, i) => 150 * (i+1)
    }).add({
        targets: '.landing-title-text .letter',
        opacity: [0,1],
        easing: "easeInOutQuad",
        duration: 800,
        delay: (el, i) => 150 * (i+1)
    });
}