const quotes = [
    "The Only limit to our realization of tomorrow is our doubt of today ",
    "Do What you can , with What you have , Where you are.",
    "The Purpose of our lives is to be happy",
    "In the Middle of Every difficulty the Oppurtunity."
]
function generateQuote(){
    const randomIndex = Math.floor(Math.random() * quotes.length);
    document.getElementById("quote").innerText = quotes[randomIndex];
}