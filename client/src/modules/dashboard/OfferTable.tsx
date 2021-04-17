const OfferTable = ({ }) => (
    
        <div className="w-full xl:w-8/12 mb-12 xl:mb-0 px-4">
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
                            <tr>
                                <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4 text-left">
                                    Aiden
                        </th>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    4,569
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    340
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                Trade
                      </button>
                        </td>
                            </tr>
                            <tr>
                                <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4 text-left">
                                    Warren
                        </th>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    3,985
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    319
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                Trade
                      </button>
                        </td>
                            </tr>
                            <tr>
                                <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4 text-left">
                                    Tayab
                        </th>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    3,513
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    294
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                Trade
                      </button>
                        </td>
                            </tr>
                            <tr>
                                <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4 text-left">
                                    Google Display Name
                        </th>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    2,050
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    147
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                Trade
                      </button>
                        </td>
                            </tr>
                            <tr>
                                <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4 text-left">
                                    Fahim
                        </th>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    1,795
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                    190
                        </td>
                                <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-white text-xs whitespace-nowrap p-4">
                                <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                Trade
                      </button>
                        </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

)

export default OfferTable;