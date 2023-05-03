import Logo from "./Logo";
import '../styles/AnonHeader.css';
import Search from "./Search";
import SignUpLogin from "./SignupLoginButton";

const AnonHeader = () => {
    return ( 
        <div className="Anon-header">
        <Logo />
        <Search />
        <SignUpLogin />
        </div>
     );
}
 
export default AnonHeader;