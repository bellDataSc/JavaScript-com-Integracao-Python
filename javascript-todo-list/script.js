function adicionarTarefa() {
    const tarefaInput = document.getElementById("tarefa");
    const texto = tarefaInput.value;
    if (texto === "") return;

    const li = document.createElement("li");
    li.textContent = texto;
    li.onclick = () => li.remove();

    document.getElementById("lista").appendChild(li);
    tarefaInput.value = "";
}
