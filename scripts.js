let score = 0;
let cardCount = {
  unacceptable: 0,
  high: 0,
  low: 0,
};

const cardsData = [
  {
    description:
      "A facial recognition AI system used for real-time biometric identification in publicly accessible spaces.",
    answer: "unacceptable",
  },
  {
    description:
      "A facial recognition AI system used for post-event biometric identification in publicly accessible spaces.",
    answer: "high",
  },
  {
    description:
      "A facial recognition AI system used for biometric identification in private spaces.",
    answer: "high",
  },
  {
    description:
      "A facial recognition AI system used by law enforcement to assess the risk of a person reoffending.",
    answer: "high",
  },
  {
    description:
      "A facial recognition AI system used by law enforcement to evaluate the reliability of evidence in criminal investigations.",
    answer: "high",
  },
  {
    description:
      "A facial recognition AI system used for identity verification in immigration, asylum, and border control management.",
    answer: "high",
  },
  {
    description:
      "A facial recognition AI system used for evaluating the eligibility of individuals for public assistance benefits and services.",
    answer: "high",
  },
  {
    description:
      "A facial recognition AI system used in the recruitment or selection process of a job.",
    answer: "high",
  },
  {
    description:
      "A facial recognition AI system used for the purpose of determining access to educational and vocational training institutions.",
    answer: "high",
  },
  {
    description:
      "A facial recognition AI system used for the management and operation of critical infrastructure, such as traffic management.",
    answer: "high",
  },
  {
    description:
      "A facial recognition AI system used to unlock a personal smartphone.",
    answer: "low",
  },
  {
    description:
      "A facial recognition AI system used to tag friends in personal photos on social media.",
    answer: "low",
  },
  {
    description:
      "A facial recognition AI system used to personalize user experience in a digital platform.",
    answer: "low",
  },
  {
    description:
      "A facial recognition AI system used for age verification on a website selling age-restricted goods.",
    answer: "low",
  },
  {
    description:
      "A facial recognition AI system used for patient identification in a private hospital setting.",
    answer: "low",
  },
  {
    description:
      "A facial recognition AI system used in a home security system.",
    answer: "low",
  },
  {
    description:
      "A facial recognition AI system used for employee check-in at a privately owned company.",
    answer: "low",
  },
  {
    description:
      "A facial recognition AI system used for personalizing advertisements on a digital platform.",
    answer: "low",
  },
  {
    description:
      "A facial recognition AI system used for identifying individuals in personal event videos.",
    answer: "low",
  },
  {
    description:
      "A facial recognition AI system used for finding look-alike faces in a celebrity database.",
    answer: "low",
  },
  {
    description:
      "A facial recognition AI system used for mass surveillance in public spaces.",
    answer: "unacceptable",
  },
  {
    description:
      "A facial recognition AI system used for real-time identification of individuals in a crowd without their consent.",
    answer: "unacceptable",
  },
  {
    description:
      "A facial recognition AI system used for determining individuals' political affiliations or religious beliefs.",
    answer: "unacceptable",
  },
  {
    description:
      "A facial recognition AI system used for making automated decisions about individuals' eligibility for social benefits.",
    answer: "unacceptable",
  },
  {
    description:
      "A facial recognition AI system used for predicting individuals' future behavior or likelihood of committing a crime.",
    answer: "unacceptable",
  },
  {
    description:
      "A facial recognition AI system used for determining individuals' credit scores or financial trustworthiness.",
    answer: "unacceptable",
  },
  {
    description:
      "A facial recognition AI system used for making automated hiring decisions without human oversight.",
    answer: "unacceptable",
  },
  {
    description:
      "A facial recognition AI system used for profiling individuals based on their appearance or ethnicity.",
    answer: "unacceptable",
  },
  {
    description:
      "A facial recognition AI system used for making automated decisions about individuals' health or medical treatment.",
    answer: "unacceptable",
  },
  {
    description:
      "A facial recognition AI system used for creating deepfakes or manipulating individuals' images without their consent.",
    answer: "unacceptable",
  },
];
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

const shuffledData = shuffleArray(cardsData);
const selectedCards = shuffledData.slice(0, 15);

selectedCards.forEach((card, index) => {
  const newCard = document.createElement("div");
  newCard.classList.add("card");
  newCard.id = `card${index}`;
  newCard.draggable = true;
  newCard.textContent = card.description;
  newCard.dataset.answer = card.answer;
  document.getElementById("cardsContainer").appendChild(newCard);
});

document.querySelectorAll(".card").forEach((card) => {
  card.addEventListener("dragstart", dragStart);
});

// Assign event listeners to the deposit areas
document.querySelectorAll(".depositArea").forEach((depositArea) => {
  depositArea.addEventListener("dragover", dragOver);
  depositArea.addEventListener("drop", drop);
});

function dragStart(e) {
  e.dataTransfer.setData("cardId", e.target.id);
}

function dragOver(e) {
  e.preventDefault();
}

function drop(e) {
  e.preventDefault();
  const cardId = e.dataTransfer.getData("cardId");
  const card = document.getElementById(cardId);
  if (e.target.classList.contains("depositArea")) {
    e.target.nextElementSibling.appendChild(card);
    if (card.dataset.answer === "unacceptable") {
      card.style.backgroundColor = "red";
    } else if (card.dataset.answer === "high") {
      card.style.backgroundColor = "yellow";
    } else if (card.dataset.answer === "low") {
      card.style.backgroundColor = "green";
    }
    calculateScore(card, e.target.parentElement);
  }
}

function calculateScore(card, bucket) {
  const correctBucket =
    (card.dataset.answer === "unacceptable" && bucket.id === "bucket1") ||
    (card.dataset.answer === "high" && bucket.id === "bucket2") ||
    (card.dataset.answer === "low" && bucket.id === "bucket3");

  if (correctBucket) {
    score += 10 + cardCount[card.dataset.answer] * 2;
  } else {
    score -= 20 + cardCount[card.dataset.answer] * 4;
  }

  cardCount[card.dataset.answer]++;
  card.removeEventListener("dragstart", dragStart);
  document.getElementById("score").textContent = score;
}
