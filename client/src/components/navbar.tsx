import { Fragment, FunctionComponent, useContext, useState } from 'react';
import { Disclosure, Menu, Transition } from '@headlessui/react';
import { BellIcon, MenuIcon, XIcon, CurrencyDollarIcon } from '@heroicons/react/outline';
import ActiveLink from './ActiveLink';
import Link from 'next/link';
import { NextRouter, withRouter } from 'next/router';
import { Context, useAuth } from '../utils/context/store';
import { auth } from '../utils/firebase.utils';

const navigation = [
  { name: 'Home', href: '/', current: true },
  { name: 'Dashboard', href: '/dash', current: false },
]

function classNames(...classes) {
  return classes.filter(Boolean).join(' ')
}

type NavigationBarProps = {
  router: NextRouter
}

const NavigationBar: FunctionComponent<NavigationBarProps> = ({ router }) => {
  const { state } = useAuth()

  return (<Disclosure as="nav" className="bg-gray-800">
    {({ open }) => (
      <>
        <div className="mr-0 px-2 sm:px-6 lg:px-8">
          <div className="relative flex items-center justify-between h-16">
            <div className="absolute inset-y-0 left-0 flex items-center sm:hidden">
              {/* Mobile menu button*/}
              <Disclosure.Button className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
                <span className="sr-only">Open main menu</span>
                {open ? (
                  <XIcon className="block h-6 w-6" aria-hidden="true" />
                ) : (
                  <MenuIcon className="block h-6 w-6" aria-hidden="true" />
                )}
              </Disclosure.Button>
            </div>
            <div className="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start">
              <div className="flex-shrink-0 flex items-center">
                <img
                  className="block lg:hidden h-8 w-auto"
                  src="/default-isolated.svg"
                  alt="Workflow"
                />
                <img
                  className="hidden lg:block h-8 w-auto"
                  src="/default-logo-white.svg"
                  alt="Workflow"
                />
              </div>
              <div className="hidden sm:block sm:ml-6">
                <div className="flex space-x-4">
                  {navigation.map((item) => (
<Link href={item.href}>
                    <a
                      key={item.name}
                      href={item.href}
                      className={classNames(
                        router.pathname === item.href ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white',
                        'px-3 py-2 rounded-md text-sm font-medium'
                      )}
                      aria-current={router.pathname === item.href ? 'page' : undefined}
                    >
                      {item.name}
                    </a>
                    </Link>
                  ))}
                </div>
              </div>
            </div>
            {state.authData != null &&
              <div className="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
              <div className="flex items-center">
                <span className="text-gray-300 px-3 py-2 rounded-md text-sm font-medium">300</span>
                <img src="/default-isolated.svg" alt="CoinCoin SVG Logo" className="h-6 w-6 ml-0" />
              </div>

              {/* Profile dropdown */}
              <Menu as="div" className="ml-3 relative z-10">
                {({ open }) => (
                  <>
                    <div>
                      <Menu.Button className="bg-gray-800 flex text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white">
                        <span className="sr-only">Open user menu</span>
                        <img
                          className="h-8 w-8 rounded-full"
                          src={state.authData.photoURL}
                          alt=""
                        />
                      </Menu.Button>
                    </div>
                    <Transition
                      show={open}
                      as={Fragment}
                      enter="transition ease-out duration-100"
                      enterFrom="transform opacity-0 scale-95"
                      enterTo="transform opacity-100 scale-100"
                      leave="transition ease-in duration-75"
                      leaveFrom="transform opacity-100 scale-100"
                      leaveTo="transform opacity-0 scale-95"
                    >
                      <Menu.Items
                        static
                        className="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
                      >

                        <Menu.Item>
                          {({ active }) => (
                            <a
                              href="#"
                              className={classNames(
                                active ? 'bg-gray-100' : '',
                                'block px-4 py-2 text-sm text-gray-700'
                              )}
                              onClick={() => auth.signOut()}
                            >
                              Sign out
                            </a>
                          )}
                        </Menu.Item>
                      </Menu.Items>
                    </Transition>
                  </>
                )}
              </Menu>
            </div>}
          </div>
        </div>

        <Disclosure.Panel className="sm:hidden">
          <div className="px-2 pt-2 pb-3 space-y-1">
            {navigation.map((item) => (
              <a
                key={item.name}
                href={item.href}
                className={classNames(
                  item.current ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white',
                  'block px-3 py-2 rounded-md text-base font-medium'
                )}
                aria-current={item.current ? 'page' : undefined}
              >
                {item.name}
              </a>
            ))}
          </div>
        </Disclosure.Panel>
      </>
    )}
  </Disclosure>)
};

export default withRouter(NavigationBar);