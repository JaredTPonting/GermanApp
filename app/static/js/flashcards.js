  // Get references to the wrapper and card elements.
  const wrapper = document.getElementById('flashcard-wrapper');
  const card = document.getElementById('flashcard');
  let currentCardId = {{ card.id }};

  let isDragging = false;
  let startX = 0;
  let currentX = 0;
  let translateX = 0;
  const swipeThreshold = 100; // Minimum drag distance (in pixels) to register a swipe

  // Handle click on the card: if not dragging, flip the card.
  function handleClick(e) {
    // Prevent the click if a drag occurred.
    if (!isDragging) {
      card.classList.toggle('flipped');
    }
  }

  // --- Mouse Events for Dragging ---
  wrapper.addEventListener('mousedown', function(e) {
    isDragging = false;
    startX = e.clientX;
    wrapper.style.transition = "none"; // Disable transitions during drag
  });

  wrapper.addEventListener('mousemove', function(e) {
    if (startX === 0) return;
    currentX = e.clientX;
    const dx = currentX - startX;
    if (Math.abs(dx) > 5) {
      isDragging = true;
    }
    if (isDragging) {
      translateX = dx;
      // Rotate a bit based on the drag distance.
      const rotate = dx / 10;
      wrapper.style.transform = `translateX(${dx}px) rotate(${rotate}deg)`;
    }
  });

  wrapper.addEventListener('mouseup', function(e) {
    endDrag();
  });

  wrapper.addEventListener('mouseleave', function(e) {
    if (isDragging) {
      endDrag();
    }
  });

  function endDrag() {
    if (!isDragging) {
      // No drag detected, let the click handler handle the flip.
      resetDrag();
      return;
    }
    // Check if the card was dragged far enough to count as a swipe.
    if (translateX > swipeThreshold) {
      // Swipe right: mark as correct.
      wrapper.style.transition = "transform 0.5s";
      wrapper.style.transform = "translateX(1000px) rotate(45deg)";
      updateCard(true);
      resetAfterSwipe();
    } else if (translateX < -swipeThreshold) {
      // Swipe left: mark as incorrect.
      wrapper.style.transition = "transform 0.5s";
      wrapper.style.transform = "translateX(-1000px) rotate(-45deg)";
      updateCard(false);
      resetAfterSwipe();
    } else {
      // Not enough drag; snap back to center.
      wrapper.style.transition = "transform 0.3s";
      wrapper.style.transform = "";
    }
    resetDrag();
  }

  function resetDrag() {
    startX = 0;
    isDragging = false;
    translateX = 0;
  }

  // --- Touch Events for Mobile Devices ---
  let touchStartX = 0;
  let touchCurrentX = 0;
  wrapper.addEventListener('touchstart', function(event) {
    touchStartX = event.changedTouches[0].screenX;
    wrapper.style.transition = "none";
  }, false);

  wrapper.addEventListener('touchmove', function(event) {
    touchCurrentX = event.changedTouches[0].screenX;
    const dx = touchCurrentX - touchStartX;
    wrapper.style.transform = `translateX(${dx}px) rotate(${dx / 10}deg)`;
  }, false);

  wrapper.addEventListener('touchend', function(event) {
    const dx = touchCurrentX - touchStartX;
    if (Math.abs(dx) > swipeThreshold) {
      if (dx > 0) {
        wrapper.style.transition = "transform 0.5s";
        wrapper.style.transform = "translateX(1000px) rotate(45deg)";
        updateCard(true);
      } else {
        wrapper.style.transition = "transform 0.5s";
        wrapper.style.transform = "translateX(-1000px) rotate(-45deg)";
        updateCard(false);
      }
      resetAfterSwipe();
    } else {
      wrapper.style.transition = "transform 0.3s";
      wrapper.style.transform = "";
    }
  }, false);

// Function to load a new random card.
function loadNextCard() {
  fetch('/learning/random_card')
    .then(response => response.json())
    .then(data => {
      // Update the card text
      document.querySelector('.flashcard .front').innerText = data.german;
      document.querySelector('.flashcard .back').innerText = data.translation;
      // Update the current card id
      currentCardId = data.id;
      // Reset any inline styles from the previous swipe
      document.getElementById('flashcard-wrapper').style.transition = "none";
      document.getElementById('flashcard-wrapper').style.transform = "";
      // Ensure the card shows the front side.
      document.getElementById('flashcard').classList.remove('flipped');
    });
}

  // Function to reset the card position and clear any flipped state after a swipe.
  function resetAfterSwipe() {
    setTimeout(() => {
      // Reset the wrapper position.
      wrapper.style.transition = "none";
      wrapper.style.transform = "";
      // Remove the flipped state so the new card shows the front.
      card.classList.remove('flipped');
      // load the next card here.
      loadNextCard();
    }, 500); // Should match the swipe animation duration.
  }

  // Placeholder function to update card data on the backend.
  function updateCard(correct) {
    console.log("Card marked as", correct ? "correct" : "incorrect");
    // Here you would use fetch/AJAX to update the card data (e.g., seen count, correct count)
    // Example:
    // fetch('/learning/update_card', {
    //   method: 'POST',
    //   headers: {'Content-Type': 'application/json'},
    //   body: JSON.stringify({card_id: {{ card.id }}, correct: correct})
    // })
    // .then(response => response.json())
    // .then(data => {
    //   // Load next card or update UI as needed.
    // });
  }