// import logo from './logo.svg';
import './App.css';
import Advertisement from './components/Advertisement';
import AnonHeader from './components/AnonHeader';
import Footer from './components/Footer';
import TrendingNews from './components/TrendingNews';
import WeeklyCountdown from './components/WeeklyCountdown';
function App() {
  return (
    <div className="grid-container">
      <div className="grid-item header"><AnonHeader /></div>
      <div className="grid-item trending-news"><TrendingNews /></div>
      <div className="grid-item weekly-countdown"><WeeklyCountdown /></div>
      <div className="grid-item advertisement"><Advertisement /></div>
      <div className="grid-item advertisement"><Footer /></div>
    </div>
     );
    
}

export default App;
