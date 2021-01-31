function shuffleTickers() {
    var tickers = document.getElementsByClassName('ticker-row');
    var element1 = Math.floor(Math.random()*6);
    var element2 = Math.floor(Math.random()*6);
    tickers[element1].parentNode.insertBefore(tickers[element1], tickers[element2]);
}
