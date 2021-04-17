import { FunctionComponent } from "react";

type FlexCardProps = {
  caption: string,
  title: string,
  description?: string,
  imageURL?: string,
}

const FlexCard: FunctionComponent<FlexCardProps> = ({ title, caption, description, imageURL, children }) => (
    <div className="w-full lg:w-6/12 xl:w-3/12 px-4 flex-grow h-full">
                  <div className="relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg">
                    <div className="flex-auto p-4">
                      <div className="flex flex-wrap">
                        <div className="relative w-full mb-4 pr-4 max-w-full flex-grow flex-1">
                          <span className="font-semibold text-xl text-purple-900">
                            {title}
                          </span>

                          <p className="text-base font-normal leading-relaxed mt-6 mb-2">
                            {description}
                          </p>
                        </div>
                        <div className="w-6/12 sm:w-4/12 px-4">
    <img src={imageURL} alt="Handshake" className="max-w-full max-h-36 align-middle border-none" />
  </div>
                        <div className="relative w-auto pl-4 flex-initial">
                          <div className="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full bg-blue-400">
                            <i>{children}</i>
                          </div>
                        </div>
                      </div>
                        <p className="text-sm text-blueGray-400 mt-4">
                        <span className="whitespace-nowrap">
                        <button
                                className="bg-purple-500 hover:bg-purple-600 hover:shadow text-white active:bg-indigo-600 text-xs font-bold uppercase px-8 py-3 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                type="button"
                            >
                                {caption}
                      </button>
                        </span>
                      </p>
                    </div>
                  </div>
                </div>
)

export default FlexCard;