import Link from "next/link"

import styles from "static/styles/styles_for_components/index.css"

export const intro = () => {
    <div className={styles.intro}>
        <h3 className={styles.name}>
            Коновалов Сергей Александрович
        </h3>
        <p className={styles.vacancy}>Full stack python developer</p>
        <Link href={"pages/about.js"}>About me</Link>
    </div>
}