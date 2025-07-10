import React from 'react';

export default function ExpiryDaysInput({ value, onChange }) {
  return (
    <div className="mb-3" id="expiryDaysContainer">
      <label htmlFor="expiryDays" className="form-label text-muted">
        Number of days until expiry
      </label>
      <input
        type="number"
        id="expiryDays"
        className="form-control form-control-lg"
        min="1"
        max="365"
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        required
      />
    </div>
  );
}
