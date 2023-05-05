import '../styles/Footer.css';

const Footer = () => {
    return ( 
        <div className="App-footer">
            <ul>
                <li className="copyright">&#169;{new Date().getFullYear()} ZMC. All rights reserved</li>
                <li><a href="#">Youtube</a></li>
                <li><a href="#">Instagram</a></li>
                <li><a href="#">Facebook</a></li>
                <li><a href="#">Twitter</a></li>
            </ul>
        </div>
     );
}
 
export default Footer;