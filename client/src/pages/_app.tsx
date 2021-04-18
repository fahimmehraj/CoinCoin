import NavigationBar from '../components/navbar'

import type { AppProps } from 'next/app'

import '../styles/globals.css'
import Footer from '../components/Footer'
import Store, { useAuth } from '../utils/context/store'
import { useEffect } from 'react'
import { signInAction } from '../utils/constants'
import { auth } from '../utils/firebase.utils'

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <Store>
      <div className="relative h-screen bg-gray-100">
        <NavigationBar />
        <Component {...pageProps} />
        <Footer />
      </div>
    </Store>
  )
}

export default MyApp
