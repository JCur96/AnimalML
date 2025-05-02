function loadClasses() {
    const dataset = document.getElementById("datasetSelection").value;
    
    // Fetch dataset classes from the server using AJAX
    if (dataset) {
        fetch(`/fetch_classes?dataset=${dataset}`)
            .then(response => response.json())
            .then(classes => updateClassList(classes));
    } else {
        document.getElementById("classSelectionContainer").style.display = "none";
    }
}

function updateClassList(classes) {
    const classListContainer = document.getElementById("classList");
    classListContainer.innerHTML = "";  // Clear previous entries
    classes.forEach(function(className) {
        const li = document.createElement("li");
        li.classList.add("list-group-item");
        li.textContent = className;
        classListContainer.appendChild(li);
    });

    // Show the class selection container
    document.getElementById("classSelectionContainer").style.display = "block";
}

// Handle the "Build Database" button click
document.getElementById("buildDatabaseBtn").addEventListener("click", function() {
    // Send an AJAX request to the /build_database endpoint
    fetch("/build_database", {
        method: "GET",  // Using GET method for this action
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);  // Show success message to user
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error occurred while building the database.");
    });
});

// Handle the "Build Lila Metadata" button click
document.getElementById("buildLilaMetadataBtn").addEventListener("click", function() {
    // Send an AJAX request to the /build_lila_metadata endpoint
    fetch("/build_lila_metadata", {
        method: "GET",  // Using GET method for this action
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);  // Show success message to user
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error occurred while building the Lila metadata.");
    });
});
