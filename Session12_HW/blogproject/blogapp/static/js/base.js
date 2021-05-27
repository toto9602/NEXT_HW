const OpenClose = () => {
    if (document.querySelector('.in_bar').style.display === 'flex') {
        document.querySelector('.in_bar').style.display = 'none';
        document.querySelector('#toggle').textContent = 'Menus';
    }
    else {
        document.querySelector('.in_bar').style.display = 'flex';
        document.querySelector('#toggle').textContent = 'Fold';
    }
}