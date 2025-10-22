def test_socketio_player_move_event():
    # Import the standalone Socket.IO app from main.py
    try:
        from flask_socketio import SocketIOTestClient  # type: ignore
        from main import app as sio_app, socketio as sio  # type: ignore
    except Exception as exc:  # pragma: no cover - if not present, skip
        import pytest

        pytest.skip(f"Socket.IO app not available: {exc}")

    client: SocketIOTestClient = sio.test_client(sio_app)
    assert client.is_connected()

    client.emit("player_move", {"move": "x1-y2"})
    received = client.get_received()

    assert any(
        pkt.get("name") == "move_result"
        and pkt.get("args")
        and isinstance(pkt["args"], list)
        and pkt["args"][0].get("result") == "Ход принят!"
        for pkt in received
    )

    client.disconnect()
