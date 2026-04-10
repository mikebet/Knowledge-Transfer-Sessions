document.getElementById("contactForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  // Clear previous messages
  document.getElementById("successMessage").classList.add("hidden");
  document.getElementById("errorMessage").classList.add("hidden");

  // Collect form data
  const formData = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    id: document.getElementById("id").value,
    phone: document.getElementById("phone").value,
  };

  try {
    const response = await fetch("/api/submissions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });

    const result = await response.json();

    if (response.ok) {
      // Success
      document.getElementById("contactForm").reset();
      document.getElementById("successMessage").classList.remove("hidden");
    } else {
      // Validation errors
      if (result.errors) {
        // Display field-level errors
        Object.keys(result.errors).forEach((field) => {
          const errorElement = document.getElementById(`${field}Error`);
          if (errorElement) {
            errorElement.textContent = result.errors[field];
          }
        });
        document.getElementById("errorMessage").textContent =
          result.message || "Please correct the highlighted fields.";
        document.getElementById("errorMessage").classList.remove("hidden");
      } else {
        document.getElementById("errorMessage").textContent =
          result.message || "An error occurred.";
        document.getElementById("errorMessage").classList.remove("hidden");
      }
    }
  } catch (error) {
    document.getElementById("errorMessage").textContent =
      "Network error: " + error.message;
    document.getElementById("errorMessage").classList.remove("hidden");
  }
});

// Clear field errors on input
["name", "email", "id", "phone"].forEach((field) => {
  document.getElementById(field).addEventListener("input", () => {
    document.getElementById(`${field}Error`).textContent = "";
  });
});
