const input = document.getElementById("searchInput");
const suggestionsList = document.getElementById("suggestions");
const exactOutput = document.getElementById("exactOutput");
const searchBtn = document.getElementById("searchBtn");

let timer;

input.addEventListener("input", () => {
  clearTimeout(timer);
  const prefix = input.value.trim();
  if (prefix === "") {
    suggestionsList.innerHTML = "";
    return;
  }

  timer = setTimeout(() => {
    fetch(`http://127.0.0.1:5000/api/prefix?prefix=${prefix}`)
      .then((res) => res.json())
      .then((data) => {
        suggestionsList.innerHTML = "";
        data.suggestions.forEach((word) => {
          const li = document.createElement("li");
          li.textContent = word;
          li.addEventListener("click", () => {
            input.value = word;
          });
          suggestionsList.appendChild(li);
        });
      });
  }, 400);
});

searchBtn.addEventListener("click", () => {
  const word = input.value.trim();
  if (!word) return;
  fetch(`http://127.0.0.1:5000/api/exact?word=${word}`)
    .then((res) => res.json())
    .then((data) => {
      if (data.frequency) {
        exactOutput.textContent = `Word: ${data.word} | Frequency: ${data.frequency}`;
      } else {
        exactOutput.textContent = data.message;
      }
    });
});
