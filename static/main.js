function openModal() {
    document.getElementById('modal').classList.remove('hidden');
    document.getElementById('overlay').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('modal').classList.add('hidden');
    document.getElementById('overlay').classList.add('hidden');
}