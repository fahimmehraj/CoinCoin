import firebase from 'firebase/app'
import { Dispatch } from 'react'

type UserData = null | firebase.User

export type State = {
    authData: UserData
}

export interface Context {
    state: State
    dispatch: Dispatch<Action>
}

export enum ActionKind {
    signIn = 'AUTHENTICATE',
    signOut = "LOGOUT",
}

export type Action = {
    type: ActionKind,
    payload: UserData
}

export const signInAction = (user: firebase.User): Action => ({
    type: ActionKind.signIn,
    payload: user,
})

export const signOutAction: Action = {
    type: ActionKind.signOut,
    payload: null,
}