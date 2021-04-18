import DashboardPage from "../modules/dashboard/DashboardPage";
import { useAuth } from "../utils/context/store";

const Dashboard = () => {
    const { state } = useAuth()
    
    if (state.authData != null) {
        return <DashboardPage />
    } else {
        return <h1 className="text-red-400">{process.env.NEXT_PUBLIC_TEST}</h1>
    }
}

export default Dashboard;