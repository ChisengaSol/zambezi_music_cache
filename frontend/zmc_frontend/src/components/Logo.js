import logo from '../assets/images/logo.png';
import '../styles/Logo.css';
const Logo = () => {
    return (  
        <div className="Logo-div">
            <img src={logo} alt="Logo" className="logo" />
        </div>
    );
}
 
export default Logo;