// Get all cards and buckets
let cards = document.getElementsByClassName("card");
let buckets = document.getElementsByClassName("bucket");

// Assign event listeners to the cards
for (let i = 0; i < cards.length; i++) {
  cards[i].addEventListener("dragstart", function (event) {
    event.dataTransfer.setData("text", event.target.id);
  });

  cards[i].addEventListener("dragend", function (event) {
    // Reassign draggable events to the cards
    let cardsInBucket = event.target.parentNode.getElementsByClassName("card");
    for (let j = 0; j < cardsInBucket.length; j++) {
      cardsInBucket[j].setAttribute("draggable", true);
      cardsInBucket[j].addEventListener("dragstart", function (event) {
        event.dataTransfer.setData("text", event.target.id);
      });
    }
  });
}

// Assign event listeners to the buckets
for (let i = 0; i < buckets.length; i++) {
  buckets[i].addEventListener("dragover", function (event) {
    event.preventDefault();
  });

  buckets[i].addEventListener("drop", function (event) {
    event.preventDefault();
    if (event.target.className === "bucket") {
      let data = event.dataTransfer.getData("text");
      event.target.appendChild(document.getElementById(data));
    }
  });
}

let submitButton = document.getElementById("submit");

submitButton.addEventListener("click", function () {
  // Save to local storage and JSON file
  let dataToSave = {};
  for (let i = 0; i < buckets.length; i++) {
    let bucketId = buckets[i].id;
    let bucketContent = buckets[i].innerHTML;
    dataToSave[bucketId] = bucketContent;

    // Save to local storage
    localStorage.setItem(bucketId, bucketContent);
  }

  // Save to JSON file
  let dataToSaveJson = JSON.stringify(dataToSave);
  let a = document.createElement("a");
  a.href =
    "data:text/plain;charset=utf-8," + encodeURIComponent(dataToSaveJson);
  a.download = "buckets.json";
  a.style.display = "none";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
});
