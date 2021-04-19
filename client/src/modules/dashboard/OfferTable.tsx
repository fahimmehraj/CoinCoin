import { gql, useQuery } from "@apollo/client";
import { useState } from "react";
import client from "../../utils/apollo-client";
import { useAuth } from "../../utils/context/store";

const OfferTable = ({ }) => {
    const OFFER_QUERY = gql`
    query offers {
        offers
      }
    `

    const TRANSACTION_QUERY = gql`
    query transaction($offerID: Int!, $userID: String!) {
        transaction(offerID: $offerID, userID: $userID)
    }
    `
    const [refreshState, refresh] = useState(0)

    const { state } = useAuth()
      const { data } = useQuery(OFFER_QUERY);

       return (<div className="w-full xl:w-8/12 mb-12 xl:mb-0 px-4">
            <div className="relative flex flex-col min-w-0 break-words bg-gray-800 w-full mb-6 shadow-lg rounded">
                <div className="rounded-t mb-0 px-4 py-3 border-0">
                    <div className="flex flex-wrap items-center">
                        <div className="relative w-full px-4 pl-0 max-w-full flex-grow flex-1">
                            <h3 className="font-semibold text-base text-white">
                            Offers
                      </h3>
                        </div>
                    </div>
                </div>
                <div className="block w-full overflow-x-auto overflow-y-auto h-96">
                    {/* Projects table */}
                    <table className="min-w-full divide-y divide-gray-700">
                        <thead>
                            <tr>
                                <th className="px-6 bg-blueGray-50 text-white align-middle border border-solid border-gray-600 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                                    User
                        </th>
                                <th className="px-6 bg-blueGray-50 text-white align-middle border border-solid border-gray-600 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                                    USD to buy CoinCoin
                        </th>
                                <th className="px-6 bg-blueGray-50 text-white align-middle border border-solid border-gray-600 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                                    CoinCoin to buy USD
                        </th>
                                <th className="px-6 bg-blueGray-50 text-white align-middle border border-solid border-gray-600 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                                    Buy
                        </th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-gray-700">
                            {data && data.offers.map((offer) => (
                                <tr>
                                    <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4 text-left">{offer.displayName}</th>
                                    <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    {offer.USD_Offer}
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    {offer.coin_Offer}
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                                onClick={async() => {
                                    console.log(offer.OfferID)
                                    console.log(state.authData.uid)
                                    const { data } = await client.query({ query: TRANSACTION_QUERY, variables: { offerID: offer.OfferID, userID: state.authData.uid }});
                                    console.log(data)
                                    refresh(3)
                                }}
                            >
                                Trade
                      </button>
                        </td>
                            </tr>

                            ))}
                            
                        </tbody>
                    </table>
                </div>
            </div>
        </div>)

};

export default OfferTable;