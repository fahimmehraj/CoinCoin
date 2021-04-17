import React from 'react';
import FlexCard from '../../components/FlexCard';
import OfferTable from './OfferTable';
import OfferTradeCard from './OfferTradeCard';

const CursorClickComponent = () => <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122" />
</svg>

const PlusCircleComponent = () => <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
</svg>

const DashboardPage = () => (

    <main>
        <div className="flex flex-wrap mt-4">
            <OfferTable />
            <OfferTradeCard />
        </div>
        <div className="flex justify-center">
            <FlexCard title="Mine CoinCoins" caption="Click to Mine" description="Simply click the button below to mine CoinCoins free of charge. All it takes is some finger grease to become rich with crypto!" imageURL="https://i.pinimg.com/originals/d1/48/c8/d148c8ec1b1a7603bfa5ee4ff43f2732.png">
                <CursorClickComponent />
            </FlexCard>
            <FlexCard title="Create New Offer" caption="Go to Creation" description="Create a new offer to potentially recieve CoinCoins from people that view and respond to your offer." imageURL="https://www.pngkey.com/png/full/49-495655_handshake-icon-handshake-graphic.png">
                <PlusCircleComponent />
            </FlexCard>
        </div>
    </main>

);

export default DashboardPage;