import { useContext, useEffect } from "react";
import { signInAction } from "../../utils/constants";
import { Context, useAuth } from "../../utils/context/store";
import { auth, signInWithGoogle } from "../../utils/firebase.utils";

const LandingPage = () => {
    const { state } = useAuth()

    return (<main>
        <section className="absolute w-full h-full">
          <div className="container mx-auto px-4 h-full">
            <div className="flex content-center items-center justify-center h-full">
              <div className="w-full lg:w-4/12 px-4">
                <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-300 border-0">
                  <div className="rounded-t mb-0 px-6 py-6">
                    <hr className="mt-6 border-b-1 border-gray-400" />
                  </div>
                  <div className="flex-auto px-4 lg:px-10 py-10 pt-0">

                      <div className="text-center mt-6">
                        <button
                          className="bg-gray-900 text-white active:bg-gray-700 text-sm font-bold px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full disabled:opacity-50"
                          type="button"
                          style={{ transition: "all .15s ease" }}
                          onClick={signInWithGoogle}
                          disabled={state.authData != null}
                        >
                          Sign In with Google
                        </button>
                      </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>)
}

export default LandingPage;