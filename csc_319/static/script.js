const navLinks = document.getElementById('navLinks')
const navMenuLinks = document.getElementById('navMenuLinks')
const biList = document.getElementById('bi-list') 

const showMenu = () => {

    if (navMenuLinks.style.display == 'none') {
        navMenuLinks.style.display = 'block'
        biList.style.display = 'none'
    }
}

const hideMenu = () => {
    
    if (navMenuLinks.style.display == 'block') {
        navMenuLinks.style.display = 'none'
        biList.style.display = 'block'
    }
}