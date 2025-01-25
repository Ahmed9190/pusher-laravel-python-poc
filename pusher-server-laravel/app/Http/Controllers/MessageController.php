<?php

namespace App\Http\Controllers;

use App\Events\MessageEvent;
use Illuminate\Http\Request;

class MessageController extends Controller
{
    public function sendMessage(Request $request)
    {
        $message = $request->input('message');

        // Broadcast the message
        broadcast(new MessageEvent($message));

        return response()->json(['status' => 'Message broadcasted!', 'message' => $message]);
    }
}
