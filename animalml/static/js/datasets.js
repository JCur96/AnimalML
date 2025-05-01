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
