import Footer from "components/common/Footer";
import Header from "components/header/Header";
import GlobalStyles from "lib/styles/globalStyles";
import { BrowserRouter } from "react-router-dom";
import Routing from "routes/Routing";

function App() {
	return (
		<BrowserRouter>
			<GlobalStyles />
			<Header />
			<Routing />
			<Footer />
		</BrowserRouter>
	);
}

export default App;
