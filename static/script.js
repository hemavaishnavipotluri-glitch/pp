
// SKILLS
function addSkill() {
    let input = document.getElementById("skillInput");
    let value = input.value.trim();

    if (!value) return;

    let skill = document.createElement("div");
    skill.className = "skill-btn";
    skill.innerText = value;

    // optional: click to remove skill
    skill.onclick = function () {
        skill.remove();
    };

    document.getElementById("skillsContainer").appendChild(skill);

    input.value = "";
}

// PROJECTS
function addProject() {
    let title = document.getElementById("projectTitle").value.trim();
    let desc = document.getElementById("projectDesc").value.trim();

    if (!title || !desc) return;

    let div = document.createElement("div");
    div.className = "project";
    div.innerHTML = `<h3>${title}</h3><p>${desc}</p>`;

    document.getElementById("projectContainer").appendChild(div);

    document.getElementById("projectTitle").value = "";
    document.getElementById("projectDesc").value = "";
}