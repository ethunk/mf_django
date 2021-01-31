function shuffleTickers() {
    var tickers = document.getElementsByClassName('ticker-row');
    var element1 = Math.floor(Math.random()*tickers.length);
    var element2 = Math.floor(Math.random()*tickers.length);
    tickers[element1].parentNode.insertBefore(tickers[element1], tickers[element2]);
    console.log('Shuffled Once.')
    if (element1 == element2) {
        console.log('Shuffling again.')
        shuffleTickers()
    }
}
