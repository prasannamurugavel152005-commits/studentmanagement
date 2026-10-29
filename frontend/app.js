const API_URL = window.API_BASE_URL;
const form = document.getElementById("studentForm");
const table = document.getElementById("studentTable");
const search = document.getElementById("search");
const status = document.getElementById("status");
const formTitle = document.getElementById("formTitle");
const submitButton = document.getElementById("submitButton");
const cancelEdit = document.getElementById("cancelEdit");
let editingId = null;

async function api(path = "", options = {}) {
  const response = await fetch(`${API_URL}${path}`, options);
  if (!response.ok && response.status !== 204) {
    const data = await response.json().catch(() => ({ error: "Request failed" }));
    throw new Error(Object.values(data).flat().join(" "));
  }
  return response.status === 204 ? null : response.json();
}

async function loadStudents(query = "") {
  try {
    status.textContent = "Loading students...";
    const students = await api(query ? `?search=${encodeURIComponent(query)}` : "");
    table.innerHTML = students.length ? students.map(student => `
      <tr>
        <td>${student.id}</td><td>${escapeHtml(student.name)}</td><td>${escapeHtml(student.email)}</td>
        <td>${escapeHtml(student.course)}</td><td>${student.age}</td>
        <td><div class="actions"><button class="edit" onclick="editStudent(${student.id})">Edit</button><button class="delete" onclick="deleteStudent(${student.id})">Delete</button></div></td>
      </tr>`).join("") : '<tr><td class="empty" colspan="6">No students found.</td></tr>';
    status.textContent = `${students.length} student${students.length === 1 ? "" : "s"}`;
  } catch (error) { status.textContent = error.message; }
}

function escapeHtml(value) {
  const element = document.createElement("span");
  element.textContent = value;
  return element.innerHTML;
}

form.addEventListener("submit", async event => {
  event.preventDefault();
  const student = Object.fromEntries(new FormData(form).entries());
  student.age = Number(student.age);
  try {
    submitButton.disabled = true;
    await api(editingId ? `${editingId}/` : "", {
      method: editingId ? "PUT" : "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(student)
    });
    resetForm();
    await loadStudents(search.value);
  } catch (error) { status.textContent = error.message; }
  finally { submitButton.disabled = false; }
});

async function editStudent(id) {
  try {
    const student = await api(`${id}/`);
    editingId = id;
    for (const field of ["name", "email", "course", "age"]) document.getElementById(field).value = student[field];
    formTitle.textContent = "Edit student";
    submitButton.textContent = "Save Changes";
    cancelEdit.hidden = false;
    window.scrollTo({ top: 0, behavior: "smooth" });
  } catch (error) { status.textContent = error.message; }
}

async function deleteStudent(id) {
  if (!confirm("Delete this student?")) return;
  try { await api(`${id}/`, { method: "DELETE" }); await loadStudents(search.value); }
  catch (error) { status.textContent = error.message; }
}

function resetForm() {
  form.reset(); editingId = null;
  formTitle.textContent = "Add a student";
  submitButton.textContent = "Add Student";
  cancelEdit.hidden = true;
}
cancelEdit.addEventListener("click", resetForm);
let searchTimer;
search.addEventListener("input", () => { clearTimeout(searchTimer); searchTimer = setTimeout(() => loadStudents(search.value), 250); });
loadStudents();
