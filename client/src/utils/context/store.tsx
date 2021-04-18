import React, {createContext, useContext, useEffect, useReducer} from "react";
import { Context as StateContext, signInAction, signOutAction, State } from "../constants";
import { auth } from "../firebase.utils";
import Reducer from './reducer'


const initialState: State = {
    authData: null,
};

const Store = ({children}) => {
    useEffect(() => {
        auth.onAuthStateChanged(async(user) => {
            if (user) {
                dispatch(signInAction(user))
            } else {
                dispatch(signOutAction)
            }
        })
    }, [])

    const [state, dispatch] = useReducer(Reducer, initialState);
    return (

        <Context.Provider value={{ state, dispatch }}>
            {children}
        </Context.Provider>
    )
};

export const Context = createContext<StateContext>({ state: initialState, dispatch: (action) => console.log("hi")});
export const useAuth = () => useContext(Context)
export default Store;