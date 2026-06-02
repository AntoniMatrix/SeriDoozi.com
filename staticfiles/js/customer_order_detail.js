const ORDER_ID = JSON.parse(document.getElementById("order-id-data").textContent);

const msgForm = document.getElementById("msgForm");
const textarea = document.getElementById("msgText");

// Handle Enter key
textarea.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    msgForm.requestSubmit();
  }
});

// Handle form submit
msgForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const text = textarea.value.trim();
  if (!text) return;

  try {
    await apiFetch(`/orders/${ORDER_ID}/message/`, {
      method: "POST",
      body: { message: text },
    });
    window.location.reload();
  } catch (err) {
    alert(err.message);
  }
});
