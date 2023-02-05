import styles from "static/styles/styles_for_components/header.css"

const header = () => {
    <header className={styles.header}>
        <div className={styles.conteiner}>
            <h1 className={styles.headerLogo}>
                BesP0lezny
            </h1>
            <nav className={styles.nav}>
                <ul className={styles.navMenu}>
                    <li className={styles.menuItem}>
                        <a className={styles.menuLink}>
                            <img src="static/icons/ico/about.ico"/> About
                        </a>
                    </li>
                    <li className={styles.menuItem}>
                        <a className={styles.menuLink}>
                            <img src="static/icons/ico/portfolio.ico"/> Work
                        </a>
                    </li>
                    <li className={styles.menuItem}>
                        <a className={styles.menuLink}>
                            <img src="static/icons/ico/blog.ico"/> Blog
                        </a>
                    </li>
                </ul>
            </nav>
        </div>
    </header>
};