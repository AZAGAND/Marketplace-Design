<?php

use Illuminate\Support\Facades\Route;

Route::view('/', 'welcome');

Route::view('Announcement', 'Announcement')
    ->middleware(['auth', 'verified'])
    ->name('Announcement');

Route::view('profile', 'profile')
    ->middleware(middleware: ['auth'])
    ->name('profile');

Route::view('User', 'User')
    ->middleware(middleware: ['auth'])
    ->name('User');

Route::view('Mahasiswa', 'Mahasiswa')
    ->middleware(middleware: ['auth'])
    ->name('Mahasiswa');

require __DIR__.'/auth.php';
