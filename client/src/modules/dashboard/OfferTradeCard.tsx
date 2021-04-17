const OfferTradeCard = () => (
    <div className="w-full xl:w-4/12 px-4">
        <div className="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded">
            <div className="rounded-t mb-0 px-4 py-3 bg-transparent">
                <div className="flex flex-wrap items-center">
                    <div className="relative w-full max-w-full flex-grow flex-1">
                        <h6 className="uppercase text-blueGray-400 mb-1 text-xs font-semibold">
                            Offers
                </h6>
                        <h2 className="text-blueGray-700 text-xl font-semibold">
                            Your current offers
                </h2>
                    </div>
                </div>
            </div>
            <div className="p-4 flex-auto">
                {/* Chart */}
                <div className="relative overflow-y-auto" style={{height: "333px"}}>
                <table className="min-w-full divide-y divide-gray-300">
                        <thead>
                            <tr>
                                <th className="px-6 bg-blueGray-50 align-middle border border-solid border-gray-300 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                                    USD to buy CoinCoin
                        </th>
                                <th className="px-6 bg-blueGray-50 align-middle border border-solid border-gray-300 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                                    CoinCoin to buy USD
                        </th>
                                
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-gray-300">
                            <tr>
                                
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    4,569
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    340
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                Cancel
                      </button>
                        </td>
                            </tr>
                            <tr>
                               
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    3,985
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    319
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                Cancel
                      </button>
                        </td>
                            </tr>
                            <tr>
                                
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    3,513
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    294
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                Cancel
                      </button>
                        </td>
                            </tr>
                            <tr>
                                
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    2,050
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    147
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                Cancel
                      </button>
                        </td>
                            </tr>
                            <tr>
                                
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    1,795
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    190
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                Cancel
                      </button>
                        </td>
                            </tr>
                            <tr>
                                
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    1,795
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                    190
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0  text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                Cancel
                      </button>
                        </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                
            </div>
        </div>
    </div>
)

export default OfferTradeCard;